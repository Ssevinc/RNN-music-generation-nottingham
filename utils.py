import json
from datetime import datetime
import os 

class Logger:
    def __init__(self,log_dir = "logs",experiment_name=None,params=None):
        self.timestamp= datetime.now().strftime("%Y%m%d-%H%M%S")
        self.experiment_name = experiment_name
        self.log_dir = log_dir
        os.makedirs(log_dir,exist_ok=True)

        self.log_file = os.path.join(log_dir, f"{self.experiment_name}.json")

        self.logs = {
            "experiment": self.experiment_name,
            "timestamp": self.timestamp,
            "params": params or {},
            "metrics": []
        }
    def log_params(self,params):
        self.logs["params"] = params

    def log_metrics(self,epochs, train_loss, val_loss=None,):
        self.logs["metrics"].append(
            {
                "epoch": epochs,
                "train_loss": train_loss,
                "val_loss": val_loss
            }
        )
    def save(self):
        with open(self.log_file, "w") as f:
            json.dump(self.logs,f,indent=4)
