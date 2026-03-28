# Method 1: Late Import
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    if "VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"


# Method 2: Dependency Injection
def record_spell_injected(spell_name: str,
                          ingredients: str, validator_func) -> str:
    validation_result = validator_func(ingredients)
    if "VALID" in validation_result:
        return (f"Spell recorded via injection: "
                f"{spell_name} ({validation_result})")
    return (f"Spell rejected via injection: "
            f"{spell_name} ({validation_result})")
