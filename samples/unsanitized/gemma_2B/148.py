
def bf(planet1, planet2):
    """
    Hamare solar system mein aath grah hain: sabse paas Suraj ke Mercury hai, uske baad Venus, phir Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
Ek function likho jo do grahon ke naam planet1 aur planet2 ko strings ke roop mein leta hai.
Function ko ek tuple return karna chahiye jisme saare grah hain jinke orbits planet1 aur planet2 ke orbit ke beech mein hote hain, Suraj ke nazdeek hone ke hisaab se sort kiye gaye.
Agar planet1 ya planet2 sahi grah ke naam nahi hain to function ko ek khali tuple return karna chahiye.
Udaharan
bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
bf("Earth", "Mercury") ==> ("Venus")
bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []
    if planet1 == planet2:
        return []
    if planet1 == "Mercury" and planet2 == "Venus":
        return ["Saturn", "Uranus"]
    if planet1 == "Venus" and planet2 == "Earth":
        return ["Mars", "Jupiter", "Saturn"]
    if planet1 == "Earth" and planet2 == "Mars":
        return ["Jupiter", "Saturn", "Uranus"]
    if planet1 == "Mars" and planet2 == "Jupiter":
        return ["Saturn", "Uranus", "Venus"]
    if planet1 == "Jupiter" and planet2 == "Saturn":
        return ["Uranus", "Venus", "Earth"]
    if planet1 == "Saturn" and planet2 == "Uranus":
        return ["Venus", "Earth", "Mars"]
    if planet1 == "Uranus" and planet2 == "Venus":
        return ["Earth", "Mars", "Jupiter"]
    if planet1 == "Neptune" and planet2 == "Earth":
        return ["Mars", "Jupiter", "Saturn"]
    if planet1 == "Earth" and planet2 == "Mars":
        return ["Jupiter", "Saturn", "Uranus"]
    if planet1 == "Mars" and planet2 == "Jupiter":
        return ["Saturn", "Uranus", "Venus"]
    if planet1 == "Jupiter" and planet2 == "Saturn":
        return ["Uranus", "Venus", "Earth"]
    if planet1 == "Saturn" and planet2 == "Uranus":
        return ["Venus", "Earth", "Mars"]
    if planet1 == "Uranus" and planet2 == "Venus":
        return ["Earth", "Mars", "Jupiter"]
    if planet1 == "Neptune" and planet2 == "Earth":
        return ["Mars", "Jupiter", "Saturn"]
    if planet1 == "Earth" and planet2 == "Mars":
        return ["Jupiter", "Saturn", "Uran