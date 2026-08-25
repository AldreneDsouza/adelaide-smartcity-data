# Adelaide Smart City — Real-Time Vehicle Analytics

An end to end Microsoft Fabric project I built using Adelaide Metro vehicle position data.

The solution automatically ingests new vehicle position data every 5 minutes, stores and transforms the data in a Fabric Lakehouse, and presents the results through an interactive Power BI dashboard.

![Adelaide Smart City Dashboard](Dashboard%20Screenshot.png)

The solution is designed to automatically ingest new vehicle position data every 5 minutes and provide an up-to-date view of vehicle activity across the Adelaide metropolitan network.

---

## 📊 Project Overview

This project demonstrates the complete data flow from source data to an interactive dashboard:

**GitHub → Fabric Pipeline → Lakehouse → Transformation → Semantic Model → Power BI**

The dashboard provides an operational view of:

- 🚍 Total vehicles
- 📈 Average speed
- ⚡ Maximum speed
- 🛣️ Active routes
- 📍 Live vehicle locations across Adelaide
- 🚍 Vehicle count by route
- 📊 Average speed by route

---

## 🏗️ Architecture

![Adelaide Smart City Architecture](architecture.png)

The solution follows a simple end-to-end analytics pipeline:

1. **Data Source**  
   Adelaide Metro vehicle-position data is made available through the project data source.

2. **Automated Ingestion**  
   GitHub Actions updates the raw vehicle-position data automatically, while a Microsoft Fabric pipeline ingests the latest data every 5 minutes.

3. **Data Storage**  
   The incoming data is stored in a Microsoft Fabric Lakehouse.

4. **Data Transformation**  
   A Fabric Notebook cleans and transforms the vehicle-position data and creates route-level summary information.

5. **Semantic Model**  
   The transformed data is exposed through a Power BI semantic model.

6. **Power BI Dashboard**  
   The dashboard provides interactive operational insights including vehicle locations, vehicle counts, route activity and speed metrics.


   ## 🧩 Challenges & Solution

One of the main challenges was obtaining the highest-frequency vehicle-position data directly through the Microsoft Fabric environment.

The source data was available at a higher frequency, but access to the required real-time capability was limited by the available Fabric subscription and configuration.

### Solution

Instead of stopping at static data, I designed an alternative ingestion workflow using GitHub as an intermediate data source.

The workflow:

**Vehicle Data Source → GitHub → Fabric Pipeline → Lakehouse → Transformation → Power BI**

GitHub is automatically updated with the latest vehicle-position data, and the Microsoft Fabric pipeline is scheduled to ingest the updated data every **5 minutes**.

This provided a practical near-real-time analytics solution while working within the available platform limitations.

### Key Learning

This was a useful lesson in designing data pipelines around real-world constraints. Rather than depending on a single ingestion method, I explored an alternative architecture that still allowed the dashboard to receive continuously updated data.

## 🔗 Data Source

This project uses Adelaide Metro vehicle-position data provided through the Adelaide Metro GTFS-Realtime feed.

**Official source:** [Adelaide Metro GTFS-Realtime API](https://gtfs.adelaidemetro.com.au/)

The vehicle-position feed provides current vehicle locations and related information in GTFS-Realtime format.

The source data is then passed through the GitHub and Microsoft Fabric ingestion workflow used in this project.


## 📈 Dashboard

The Power BI dashboard provides an interactive view of the current Adelaide Metro vehicle network.

### Key Metrics

- **Total Vehicles** — current number of vehicles in the dataset
- **Average Speed** — current average vehicle speed
- **Maximum Speed** — highest recorded vehicle speed
- **Active Routes** — number of routes currently represented

### Visualizations

- **Live Vehicle Locations** — interactive map of vehicle positions across Adelaide
- **Vehicles by Route** — vehicle distribution across routes
- **Average Speed by Route** — comparison of average speeds across routes

The dashboard updates as new data is processed through the automated 5-minute ingestion pipeline.
