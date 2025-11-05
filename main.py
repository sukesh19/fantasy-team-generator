import random

# Player database with positions and ratings
PLAYERS = {
    "Forward": [
        {"name": "Dragon Striker", "rating": 95},
        {"name": "Phoenix Blade", "rating": 92},
        {"name": "Thunder Fang", "rating": 88},
        {"name": "Storm Reaper", "rating": 85},
        {"name": "Shadow Hunter", "rating": 82},
        {"name": "Frost Warrior", "rating": 79},
        {"name": "Ember Knight", "rating": 76},
        {"name": "Mystic Arrow", "rating": 73},
    ],
    "Midfielder": [
        {"name": "Crystal Mage", "rating": 93},
        {"name": "Wind Dancer", "rating": 90},
        {"name": "Earth Shaker", "rating": 87},
        {"name": "Tide Turner", "rating": 84},
        {"name": "Star Weaver", "rating": 81},
        {"name": "Moon Walker", "rating": 78},
        {"name": "Sun Chaser", "rating": 75},
        {"name": "Cloud Drifter", "rating": 72},
    ],
    "Defender": [
        {"name": "Iron Wall", "rating": 91},
        {"name": "Stone Guardian", "rating": 89},
        {"name": "Steel Sentinel", "rating": 86},
        {"name": "Bronze Titan", "rating": 83},
        {"name": "Silver Shield", "rating": 80},
        {"name": "Gold Fortress", "rating": 77},
        {"name": "Diamond Bastion", "rating": 74},
        {"name": "Platinum Warden", "rating": 71},
    ],
    "Goalkeeper": [
        {"name": "Void Keeper", "rating": 94},
        {"name": "Time Stopper", "rating": 89},
        {"name": "Space Bender", "rating": 84},
        {"name": "Light Catcher", "rating": 79},
        {"name": "Dark Blocker", "rating": 74},
    ]
}

def generate_team(formation="4-4-2", team_name=None):
    """
    Generate a fantasy team with given formation.
    
    Args:
        formation: String like "4-4-2" (defenders-midfielders-forwards)
        team_name: Optional team name
    
    Returns:
        Dictionary with team details
    """
    # Parse formation
    parts = formation.split("-")
    if len(parts) != 3:
        raise ValueError("Formation must be in format 'defenders-midfielders-forwards' (e.g., '4-4-2')")
    
    num_defenders = int(parts[0])
    num_midfielders = int(parts[1])
    num_forwards = int(parts[2])
    
    # Generate team
    team = {
        "name": team_name or f"Team {random.choice(['Dragons', 'Phoenix', 'Titans', 'Warriors', 'Legends'])}",
        "formation": formation,
        "players": {
            "Goalkeeper": random.sample(PLAYERS["Goalkeeper"], 1),
            "Defenders": random.sample(PLAYERS["Defender"], num_defenders),
            "Midfielders": random.sample(PLAYERS["Midfielder"], num_midfielders),
            "Forwards": random.sample(PLAYERS["Forward"], num_forwards)
        }
    }
    
    # Calculate team rating
    all_players = (team["players"]["Goalkeeper"] + 
                   team["players"]["Defenders"] + 
                   team["players"]["Midfielders"] + 
                   team["players"]["Forwards"])
    
    team["total_rating"] = sum(p["rating"] for p in all_players)
    team["average_rating"] = round(team["total_rating"] / len(all_players), 1)
    
    return team

def print_team(team):
    """Print team in a formatted way."""
    print(f"\n{'='*50}")
    print(f"  {team['name'].upper()}")
    print(f"  Formation: {team['formation']}")
    print(f"  Average Rating: {team['average_rating']}")
    print(f"{'='*50}\n")
    
    # Goalkeeper
    print("GOALKEEPER:")
    for player in team["players"]["Goalkeeper"]:
        print(f"  • {player['name']} (Rating: {player['rating']})")
    
    # Defenders
    print("\nDEFENDERS:")
    for player in team["players"]["Defenders"]:
        print(f"  • {player['name']} (Rating: {player['rating']})")
    
    # Midfielders
    print("\nMIDFIELDERS:")
    for player in team["players"]["Midfielders"]:
        print(f"  • {player['name']} (Rating: {player['rating']})")
    
    # Forwards
    print("\nFORWARDS:")
    for player in team["players"]["Forwards"]:
        print(f"  • {player['name']} (Rating: {player['rating']})")
    
    print(f"\n{'='*50}\n")

# Example usage
if __name__ == "__main__":
    # Generate teams with different formations
    formations = ["4-4-2", "4-3-3", "3-5-2", "5-3-2"]
    
    print("FANTASY TEAM GENERATOR")
    print("=" * 50)
    
    for formation in formations:
        team = generate_team(formation=formation)
        print_team(team)
    
    # Generate a custom team
    print("\n" + "="*50)
    print("CUSTOM TEAM")
    print("="*50)
    custom_team = generate_team(formation="4-4-2", team_name="My Dream Team")
    print_team(custom_team)
