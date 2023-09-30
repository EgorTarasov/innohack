import { Ticket } from '.';

export interface Sprint {
    id: number;
    duration: number;
    target: string;
    is_finished: boolean;
    users: {
        user_data: {
            id: number;
            username: string;
            hours: number;
        };
        tickets: Ticket[];
    }[];
}
