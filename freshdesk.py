def create_ticket(subject, description):
    print(f"Demo Ticket Created: {subject} | {description}")
    return 200, {"ticket_id": "demo123"}
