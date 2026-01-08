
```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "Example Polygon" },
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[-100,40], [-90,40], [-90,30], [-100,30], [-100,40]]]
      }
    }
  ]
}
```


 $$ If $$

$$ Your $$

$$ Here $$

$$ Thanks $$


<img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/e6df613e-e91d-4512-a86a-26352c09c659" />


$$UPDATES$$

$$ COMING $$

$$SOON$$


```stl
solid cube
facet normal 0 0 -1
  outer loop
    vertex 0 0 0
    vertex 1 0 0
    vertex 1 1 0
  endloop
endfacet
facet normal 0 0 -1
  outer loop
    vertex 0 0 0
    vertex 1 1 0
    vertex 0 1 0
  endloop
endfacet
facet normal 0 0 1
  outer loop
    vertex 0 0 1
    vertex 0 1 1
    vertex 1 1 1
  endloop
endfacet
facet normal 0 0 1
  outer loop
    vertex 0 0 1
    vertex 1 1 1
    vertex 1 0 1
  endloop
endfacet
facet normal -1 0 0
  outer loop
    vertex 0 0 0
    vertex 0 0 1
    vertex 0 1 1
  endloop
endfacet
facet normal -1 0 0
  outer loop
    vertex 0 0 0
    vertex 0 1 1
    vertex 0 1 0
  endloop
endfacet
facet normal 1 0 0
  outer loop
    vertex 1 0 0
    vertex 1 1 0
    vertex 1 1 1
  endloop
endfacet
facet normal 1 0 0
  outer loop
    vertex 1 0 0
    vertex 1 1 1
    vertex 1 0 1
  endloop
endfacet
facet normal 0 -1 0
  outer loop
    vertex 0 0 0
    vertex 1 0 0
    vertex 1 0 1
  endloop
endfacet
facet normal 0 -1 0
  outer loop
    vertex 0 0 0
    vertex 1 0 1
    vertex 0 0 1
  endloop
endfacet
facet normal 0 1 0
  outer loop
    vertex 0 1 0
    vertex 0 1 1
    vertex 1 1 1
  endloop
endfacet
facet normal 0 1 0
  outer loop
    vertex 0 1 0
    vertex 1 1 1
    vertex 1 1 0
  endloop
endfacet
endsolid cube


```
```mermaid
flowchart TD
    Trigger[On: push or pull_request<br>to main branch] --> Job1[Job: Lint & Test]

    subgraph Job1
        direction TB
        Step1[Checkout code] --> Step2[Setup Node/Python/etc.]
        Step2 --> Step3[Install dependencies]
        Step3 --> Step4[Run tests]
        Step4 --> Step5[Build artifact]
    end

    Job1 -->|needs| Job2[Job: Build Docker Image]
    Job2 --> Job3[Job: Deploy to Staging]

    subgraph Job3
        direction TB
        Deploy1[SSH to server] --> Deploy2[Pull image]
        Deploy2 --> Deploy3[Restart service]
    end

    Job3 -->|on success| Job4[Job: Manual Approval<br>for Production]
    Job4 --> Job5[Job: Deploy to Production]

    style Trigger fill:#f9f,stroke:#333
    style Job4 fill:#ff9,stroke:#f66,stroke-width:2px
