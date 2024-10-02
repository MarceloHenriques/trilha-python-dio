linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"]) # no append vc adiciona item por item, com o extend ele adiciona uma nova lista de valores a lista original

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
