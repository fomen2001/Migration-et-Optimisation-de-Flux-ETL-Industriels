import polars as pl
import numpy as np
import time
from datetime import datetime, timedelta

# =================================================================
# 1. SIMULATION DU SCRIPT R D'ORIGINE (LOGIQUE MÉTIER)
# =================================================================
# En R, on utiliserait : 
# df <- read.csv("sensor_data.csv")
# df_clean <- df %>% filter(value > 0) %>% group_by(sensor_id) %>% mutate(mean_val = mean(value))

def generate_dummy_industrial_data(n=1_000_000):
    """Génère un volume important de données capteurs pour le benchmark."""
    start_date = datetime(2024, 1, 1)
    # On calcule la fin exacte pour avoir précisément 'n' lignes (n-1 secondes après le début)
    end_date = start_date + timedelta(seconds=n-1)
    
    return pl.DataFrame({
        "timestamp": pl.datetime_range(
            start=start_date, 
            end=end_date, 
            interval="1s", 
            eager=True
        ),
        "sensor_id": np.random.randint(1, 50, n),
        "reading_value": np.random.normal(100, 15, n),
        "status": np.random.choice(["OK", "FAIL", "WARN"], n)
    })

# =================================================================
# 2. MIGRATION ET OPTIMISATION (POLARS)
# =================================================================
def optimized_etl_process(df):
    """
    Migration optimisée : On utilise Polars (Lazy API) pour surpasser 
    les performances de R (base) et de Pandas.
    """
    start_time = time.time()
    
    # Utilisation du mode Lazy pour l'optimisation des requêtes
    result = (
        df.lazy()
        .filter(pl.col("status") == "OK")
        .with_columns([
            # Calcul du rendement (Yield simulation)
            (pl.col("reading_value") * 0.98).alias("calibrated_value"),
            # Moyenne mobile sur 5 périodes par capteur
            pl.col("reading_value").mean().over("sensor_id").alias("avg_sensor_perf")
        ])
        .group_by("sensor_id")
        .agg([
            pl.col("calibrated_value").mean().alias("mean_yield"),
            pl.col("status").count().alias("count_ok")
        ])
        .sort("mean_yield", descending=True)
        .collect()
    )
    
    end_time = time.time()
    print(f"✅ Migration R -> Python (Polars) terminée en {end_time - start_time:.4f} secondes.")
    return result

if __name__ == "__main__":
    print("--- Démarrage du pipeline ETL Industriel ---")
    data = generate_dummy_industrial_data()
    
    # Exécution de l'ETL
    final_metrics = optimized_etl_process(data)
    
    # Aperçu des résultats
    print(final_metrics.head(5))
    
    # Export pour l'infrastructure IT (CSV standardisé)
    final_metrics.write_csv("industrial_yield_metrics.csv")
    print("📁 Fichier 'industrial_yield_metrics.csv' prêt pour l'intégration IT.")