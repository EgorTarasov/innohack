import { makeAutoObservable, observable, runInAction } from 'mobx';
import { CreateSprintBody, Sprint, Ticket } from '../api/models';
import { TicketApiServiceInstanse } from '../api/TicketApiService';

export class RootStore {
    public trigger: boolean = false;
    public tickets: Ticket[] = [];
    public ticketsByUserRole: Ticket[] = [];

    constructor() {
        makeAutoObservable(this, {
            trigger: observable,
            tickets: observable,
            ticketsByUserRole: observable,
        });
    }

    public setTrigger() {
        runInAction(() => {
            this.trigger = !this.trigger;
        });
    }

    public setTickets(tickets: Ticket[]) {
        runInAction(() => {
            this.tickets = tickets;
        });
    }

    public setTicketsByUserRole(tickets: Ticket[]) {
        runInAction(() => {
            this.ticketsByUserRole = tickets;
        });
    }

    public async getTickets() {
        const tickets = await TicketApiServiceInstanse.getTickets();

        runInAction(() => {
            this.tickets = tickets;
        });

        return tickets;
    }

    public async getTicketsByUserRole(roleId: number) {
        const tickets = await TicketApiServiceInstanse.getTicketByRole(roleId);

        runInAction(() => {
            this.ticketsByUserRole = tickets;
        });

        return tickets;
    }

    public async changeTicketDuration(ticketId: number, body: { duration: number }): Promise<void> {
        const response = await TicketApiServiceInstanse.changeTicketDuration(
            ticketId,
            body
        ).finally(() => {
            this.getTickets();
            this.getTicketsByUserRole(12);
        });

        return response;
    }

    public async createSprint(body: CreateSprintBody): Promise<Sprint> {
        const response = await TicketApiServiceInstanse.createSprint(body).finally(() => {
            this.getTickets();
            this.getTicketsByUserRole(12);
        });

        return response;
    }

    public async getAllUsers() {
        const response = await TicketApiServiceInstanse.getAllUsers();

        return response;
    }
}
