export interface CreateSprintBody {
    target: string;
    duration: number;
    users: {
        id: number;
        hours: number;
    }[];
}
