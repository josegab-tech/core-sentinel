import subprocess

def analyze_logs():
    print("=== CORESENTINEL: PARSER E ANÁLISE DE CAUSA-RAIZ DE LOGS ===")
    try:
        # Captura stdout e stderr juntos usando stderr=subprocess.STDOUT
        result = subprocess.run(
            ["docker", "logs", "coresentinel_app"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, 
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        logs = result.stdout.splitlines()
        errors = [line for line in logs if "ERROR" in line or "FAILURE" in line]
        
        print(f"Total de falhas/erros identificados no container: {len(errors)}")
        if errors:
            print("\nÚltimos eventos críticos registrados:")
            for err in errors[-3:]:
                print(f" [CRITICAL] -> {err}")
        else:
            print("[INFO] Nenhuma falha crítica registrada nos logs recentes.")
            
    except Exception as e:
        print(f"[ERROR] Não foi possível capturar os logs do container: {e}")

if __name__ == "__main__":
    analyze_logs()