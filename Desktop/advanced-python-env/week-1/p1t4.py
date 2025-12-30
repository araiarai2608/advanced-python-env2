def is_alive(health):
    if health <= 0:
        return False
    else:
        return True
health=10
print(is_alive(health))