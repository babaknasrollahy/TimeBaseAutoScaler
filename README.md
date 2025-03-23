# Tbase (TimeBaseAutoScaler)

Tbase is a kubernetes operator for scaling pods base on time.


## Installation
The easiest way to install **Tbase operator** is its **hlem chart** . 
#### Heml chart

1. Clone the repository :

```bash
git clone https://github.com/babaknasrollahy/timebaseautoscaler.git
```
2. Go to the helm chart directory :
```bash
cd timebaseautoscaler/charts/tbase-operator
```
3. Change the **values.yaml** file (optional)
4. Install helm chart :
```bash
helm install tbase-operator -n tbase-operator .
```
#### Kubectl
You can also install **Tbase operator** by `kubectl` command :

1. Go to the **playground** directory :
```bash
cd timebaseautoscaler/playground
```
2. apply all `.yaml` files in this directory:
```bash
kubectl apply -f *.yaml
```

## Usage
For using Tbase you need to create a `TimeBaseAutoScaler` resource :
```yaml
apiVersion: sre.exalab.co/v1
kind: TimeBaseAutoScaler
metadata:
  name: <tbase-name>
spec:
  deploymentName: "<deployment-name>"
  scaleUpTime: "01:30:00"     #Time of scale up
  scaleDownTime: "23:30:00"   #Time of scale down
  scaleUpReplica: 15
  scaleDownReplica: 5
  waveOfScale: 2 
```
#### **note:** 
if you want to `ScaleUp` or `ScaleDown` as soon as creating `tbase`, you can create a `TimeBaseAutoScaler` like this :

```yaml
apiVersion: sre.exalab.co/v1
kind: TimeBaseAutoScaler
metadata:
  name: <tbase-name>
spec:
  deploymentName: "<deployment-name>"
  scaleUpTime: "-1"
  scaleDownTime: "-1"
  scaleUpReplica: 15
  scaleDownReplica: -1
  waveOfScale: 2 
# Only ScaleUp is run by this tbase
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
