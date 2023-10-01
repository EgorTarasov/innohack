import csv
import datetime

from app.models import Ticket


def csv_reader_to_tickets(csv_reader: csv.DictReader) -> list[Ticket]:
    tickets = []
    for row in csv_reader:
        print(row)
        ticket = Ticket()
        ticket.title = row['title']
        ticket.description = row['description']
        ticket.due_date = datetime.datetime.fromisoformat(row.get('due_date', None))
        ticket.reporter_id = row.get('reporter_id', None)
        ticket.role_id = row['role_id']
        ticket.level_id = row['level_id']
        ticket.created_at = datetime.datetime.now()
        ticket.updated_at = datetime.datetime.now()
        tickets.append(ticket)
    return tickets