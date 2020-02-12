from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        #insert every ticket
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        """
        The ticket with the none for source will be the first ticket
        and will start the ticket chain as the first current ticket
        """
        if ticket.source == "NONE":
            route[0] = ticket.destination
    
    current_ticket = route[0]
    ticket_pointer = 1
    
    # increment through the linked list and proceed using  current_ticket and ticket_pointer
    while route[-1] is None:
        route[ticket_pointer] = hash_table_retrieve(hashtable, current_ticket)
        current_ticket = route[ticket_pointer]
        ticket_pointer += 1

    return route