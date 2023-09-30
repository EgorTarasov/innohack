from app.models import Ticket
import csv

def csv_reader_to_tickets(csv_reader):
    tickets = []
    for row in csv_reader:
        ticket = Ticket()
        ticket.title = row['title']
        ticket.description = row['description']
        ticket.due_date = row.get('due_date', None)
        ticket.
        tickets.append(ticket)
    return tickets