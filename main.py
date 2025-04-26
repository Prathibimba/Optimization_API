from fastapi import FastAPI
from model import InputData, OutputData, MovePlan
from optimizer import build_graph, dijkstra
import time

app = FastAPI()

@app.post("/optimize", response_model=OutputData)
def optimize(input: InputData):
    start_time = time.time()
    graph = build_graph([r.dict() for r in input.routes])

    plan = []
    for c in input.containers:
        cost, path = dijkstra(graph, c.origin, c.destination)
        plan.append(MovePlan(
            containerId=c.id,
            route=path,
            totalCost=cost
        ))

    end_time = time.time()
    latency = (end_time - start_time) * 1000

    return OutputData(plan=plan, latencyMs=latency)
