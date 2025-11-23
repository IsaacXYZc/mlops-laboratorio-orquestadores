import mlflow
import requests

def configure_mlflow(tracking_uri: str, experiment_name: str):
    """
    Configura MLflow: tracking uri y experimento.
    Args:
        tracking_uri (str): URI del servidor de tracking de MLflow.
        experiment_name (str): Nombre del experimento en MLflow.
    Returns:
        bool: True si se configuro correctamente, False en caso contrario.
    """
    if not _check_tracking_uri_connection(tracking_uri):
        return False
    try:
        mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_experiment(experiment_name)
        return True
    except Exception as e:
        print(f"Error al configurar MLflow: {e}")
        return False

def _check_tracking_uri_connection(tracking_uri: str):
    try:
        response = requests.get(tracking_uri)
        return response.status_code == 200
    except Exception as e:
        print(f"Error al probar el tracking uri: {e}")
        return False