import { Level } from './Level';
import { Role } from './Role';

export interface Ticket {
    id: number;
    sprint_id: number;
    title: string;
    description: string;
    reporter_id: number;
    assignee_id: number;
    due_date: string;
    durations: number[];
    roles: Role;
    level: Level;
    priority: number;
}
