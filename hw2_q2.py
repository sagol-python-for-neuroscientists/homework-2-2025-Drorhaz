# Final version with __main__ block added
from collections import namedtuple
from enum import Enum
from itertools import zip_longest

# Define conditions and agents
Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

# Meeting rules dictionary
MEETING_RULES = {
    (Condition.CURE, Condition.SICK): (Condition.CURE, Condition.HEALTHY),
    (Condition.SICK, Condition.CURE): (Condition.HEALTHY, Condition.CURE),

    (Condition.CURE, Condition.DYING): (Condition.CURE, Condition.SICK),
    (Condition.DYING, Condition.CURE): (Condition.SICK, Condition.CURE),

    (Condition.CURE, Condition.CURE): (Condition.CURE, Condition.CURE),

    (Condition.DYING, Condition.DYING): (Condition.DEAD, Condition.DEAD),

    (Condition.SICK, Condition.DYING): (Condition.DYING, Condition.DEAD),
    (Condition.DYING, Condition.SICK): (Condition.DEAD, Condition.DYING),

    (Condition.SICK, Condition.SICK): (Condition.DYING, Condition.DYING),
}

def eligible_indices(agent_listing: tuple[Agent]) -> list[int]:
    """Returns a list of indices of agents eligible to meet."""
    return [i for i, agent in enumerate(agent_listing) if agent.category not in (Condition.HEALTHY, Condition.DEAD)]

def process_meeting_pairs(agent_listing: list[Agent], indices: list[int]) -> list[Agent]:
    """Returns a new agent list with updated categories applied to eligible pairs."""
    updated = list(agent_listing)  # Create a copy of the list
    for i, j in zip_longest(indices[::2], indices[1::2]):
        if j is not None:
            a1, a2 = updated[i], updated[j]
            new_cat1, new_cat2 = MEETING_RULES.get(
                (a1.category, a2.category),
                (a1.category, a2.category)
            )
            updated[i] = Agent(a1.name, new_cat1)
            updated[j] = Agent(a2.name, new_cat2)
    return updated

def meetup(agent_listing: tuple[Agent]) -> list[Agent]:
    # Find eligible agent indices
    indices = eligible_indices(agent_listing)

    # Process pairs and get updated full agent list
    updated_agents = process_meeting_pairs(agent_listing, indices)

    return updated_agents


if __name__ == "__main__":
    # Example input agents
    agents = (
        Agent("Alice", Condition.CURE),
        Agent("Bob", Condition.SICK),
        Agent("Charlie", Condition.HEALTHY),
        Agent("Dana", Condition.DYING),
        Agent("Eve", Condition.SICK),
        Agent("Frank", Condition.DEAD),
        Agent("Grace", Condition.CURE),
    )

    # Run simulation
    updated_agents = meetup(agents)

    # Print results
    print("Updated Agent Conditions:")
    for agent in updated_agents:
        print(f"{agent.name}: {agent.category.name}")
