try:
    raise Exception("Dzwoń po policję")
except Exception:
    print("Tutaj się jeszcze nie wywaliłem.")
raise Exception("Inny error")