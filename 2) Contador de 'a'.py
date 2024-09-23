def conta_a(texto):
    count = texto.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

# String a ser verificada
texto = "A raposa marrom rápida pula no rio"

print(conta_a(texto))