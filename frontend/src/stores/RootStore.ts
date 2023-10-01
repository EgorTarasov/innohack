import { makeAutoObservable, observable, runInAction } from "mobx";
import { CreateSprintBody, SprintI, Ticket } from "../api/models";
import { TicketApiServiceInstanse } from "../api/TicketApiService";

export class RootStore {
    public trigger: boolean = false;
    public tickets: Ticket[] = [];
    public ticketsByUserRole: Ticket[] = [];
    public sprint: SprintI | null = null;
    public isDeleteTicketAvailable: boolean = false;
    public isAddTicketAvailable: boolean = false;
    public activeSprintUserIndex: number = 0;

    constructor() {
        makeAutoObservable(this, {
            trigger: observable,
            tickets: observable,
            ticketsByUserRole: observable,
            sprint: observable,
            isAddTicketAvailable: observable,
            isDeleteTicketAvailable: observable,
            activeSprintUserIndex: observable,
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

    public setActiveSprintUserIndex(activeSprintUserIndex: number) {
        runInAction(() => {
            this.activeSprintUserIndex = activeSprintUserIndex;
        });
    }

    public setIsDeleteTicketAvailable(isDeleteTicketAvailable: boolean) {
        runInAction(() => {
            this.isDeleteTicketAvailable = isDeleteTicketAvailable;
        });
    }

    public setIsAddTicketAvailable(isAddTicketAvailable: boolean) {
        runInAction(() => {
            this.isAddTicketAvailable = isAddTicketAvailable;
        });
    }

    public addTicketToSprintByUser(
        sprintUserIndex: number,
        ticketIndex: number,
        ticket: Ticket,
    ) {
        console.log(sprintUserIndex, ticketIndex);

        runInAction(() => {
            this.sprint?.users[sprintUserIndex].tickets.push(ticket);
            // remove ticket from tickets
            this.tickets.splice(ticketIndex, 1);
            console.log(this.tickets);
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

    public async changeTicketDuration(
        ticketId: number,
        body: { duration: number },
    ): Promise<void> {
        const response = await TicketApiServiceInstanse.changeTicketDuration(
            ticketId,
            body,
        ).finally(() => {
            this.getTickets();
            // this.getTicketsByUserRole(12);
        });

        return response;
    }

    public async createSprint(body: CreateSprintBody): Promise<SprintI> {
        const response = await TicketApiServiceInstanse.createSprint(
            body,
        ).finally(() => {
            this.getTickets();
            this.getTicketsByUserRole(1);
        });

        runInAction(() => {
            this.sprint = response;
        });

        return response;
    }

    public async getAllUsers() {
        const response = await TicketApiServiceInstanse.getAllUsers();

        return response;
    }

    public async getLatestSprint(): Promise<SprintI> {
        const response = await TicketApiServiceInstanse.getLatestSprint();

        runInAction(() => {
            this.sprint = response;
        });

        return response;
    }

    public async updateSprint(body: SprintI): Promise<SprintI> {
        const response = await TicketApiServiceInstanse.updateSprint(body);

        return response;
    }

    public async importTickets(): Promise<void> {
        const response = await TicketApiServiceInstanse.importTickets().finally(
            () => {
                this.getTickets();
                this.getTicketsByUserRole(1);
            },
        );

        return response;
    }
}
