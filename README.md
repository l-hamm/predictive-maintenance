# **Will my machine break down today?** - Using a binary classifier for predictive maintenance

[Link to notebook]('PdM.ipynb')

In this repository we use data of several machines to predict whether a component of a machine breaks down within the next hours. To do so, we will first evaluate the provided data, then we will try to understand the correlations between features for a single machine. Next we will label our dataset to finally train a binary classifier model and check its performance. All steps are described in [PdM.ipynb](https://github.com/l-hamm/predictive-maintenance/blob/main/PdM.ipynb).

### The dataset consists of the following data:
- [Metadata of Machines](https://azuremlsampleexperiments.blob.core.windows.net/datasets/PdM_machines.csv): Model type & age of the Machines.

- [Telemetry Time Series Data](https://azuremlsampleexperiments.blob.core.windows.net/datasets/PdM_telemetry.csv): It consists of hourly average of voltage, rotation, pressure, vibration collected from 100 machines for the year 2015.  

- [Error](https://azuremlsampleexperiments.blob.core.windows.net/datasets/PdM_errors.csv): These are errors encountered by the machines while in operating condition. Since, these errors don't shut down the machines, these are not considered as failures. The error date and times are rounded to the closest hour since the telemetry data is collected at an hourly rate.  

- [Maintenance](https://azuremlsampleexperiments.blob.core.windows.net/datasets/PdM_maint.csv): If a component of a machine is replaced, that is captured as a record in this table. Components are replaced under two situations: 1. During the regular scheduled visit, the technician replaced it (Proactive Maintenance) 2. A component breaks down and then the technician does an unscheduled maintenance to replace the component (Reactive Maintenance). This is considered as a failure and corresponding data is captured under Failures. Maintenance data has both 2014 and 2015 records. This data is rounded to the closest hour since the telemetry data is collected at an hourly rate.  

- [Failures](https://azuremlsampleexperiments.blob.core.windows.net/datasets/PdM_failures.csv): Each record represents replacement of a component due to failure. This data is a subset of Maintenance data. This data is rounded to the closest hour since the telemetry data is collected at an hourly rate.  

**Acknowledgement**  
This dataset was available as a part of Azure AI Notebooks for Predictive Maintenance. But as of 15th Oct, 2020 the notebook (link) is no longer available. However, the data can still be downloaded using the links above.