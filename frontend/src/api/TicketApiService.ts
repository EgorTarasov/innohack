import axios from 'axios';
import { API_URL } from '../config';
import authHeader from '../utils/authHeader';
import { CreateSprintBody, Sprint, Ticket, Worker } from './models';

const sprint: Sprint = {
    id: 1,
    duration: 1,
    target: 'test',
    is_finished: false,
    users: [
        {
            user_data: {
                id: 2,
                username: 'Иван Иванов',
                hours: 20,
            },
            tickets: [
                {
                    id: 42,
                    sprint_id: 1,
                    title: 'Ticket 2 Title',
                    description: 'Ticket 2 Description',
                    reporter_id: 2,
                    assignee_id: 3,
                    due_date: '2022-01-02T00:00:00',
                    roles: { role_id: 13, label: 'Frontend' },
                    level: { level_id: 9, label: 'Senior' },
                    durations: [1, 2, 4],
                    priority: 1,
                },
                {
                    id: 42,
                    sprint_id: 1,
                    title: 'Ticket 2 Title',
                    description: 'Ticket 2 Description',
                    reporter_id: 2,
                    assignee_id: 3,
                    due_date: '2022-01-02T00:00:00',
                    roles: { role_id: 13, label: 'Frontend' },
                    level: { level_id: 9, label: 'Senior' },
                    durations: [1, 2, 4],
                    priority: 1,
                },
                {
                    id: 42,
                    sprint_id: 1,
                    title: 'Ticket 2 Title',
                    description: 'Ticket 2 Description',
                    reporter_id: 2,
                    assignee_id: 3,
                    due_date: '2022-01-02T00:00:00',
                    roles: { role_id: 13, label: 'Frontend' },
                    level: { level_id: 9, label: 'Senior' },
                    durations: [1, 2, 4],
                    priority: 1,
                },
            ],
        },
        {
            user_data: {
                id: 2,
                username: 'Иван Иванов',
                hours: 20,
            },
            tickets: [
                {
                    id: 42,
                    sprint_id: 1,
                    title: 'Ticket 2 Title',
                    description: 'Ticket 2 Description',
                    reporter_id: 2,
                    assignee_id: 3,
                    due_date: '2022-01-02T00:00:00',
                    roles: { role_id: 13, label: 'Frontend' },
                    level: { level_id: 9, label: 'Senior' },
                    durations: [1, 2, 4],
                    priority: 1,
                },
            ],
        },
    ],
};

class TicketApiService {
    public async getTickets() {
        // return [
        //     {
        //         id: 1,
        //         sprint_id: 1,
        //         title: 'ticket 1',
        //         description: 'test',
        //         reporter_id: 1,
        //         assignee_id: 2,
        //         due_date: '2021-01-01',
        //         durations: [1, 2, 4],
        //         role: { role_id: 1, label: 'Frontend' },
        //         level: { level_id: 1, label: 'Junior' },
        //         priority: 2,
        //     },
        // ];

        const response = await axios.get<Ticket[]>(`${API_URL}/ticket/all`, {
            headers: authHeader(),
        });

        return response.data;
    }

    public async getTicketByRole(roleId: number) {
        // return [
        //     {
        //         id: 41,
        //         sprint_id: 1,
        //         title: 'ticket by role',
        //         description: 'test',
        //         reporter_id: 1,
        //         assignee_id: 2,
        //         due_date: '2021-01-01',
        //         durations: [1, 2, 4],
        //         role: { role_id: 1, label: 'Frontend' },
        //         level: { level_id: 1, label: 'Junior' },
        //         priority: 2,
        //     },
        // ];

        const response = await axios.get<Ticket[]>(`${API_URL}/ticket/role/${roleId}`, {
            headers: authHeader(),
        });

        return response.data;
    }

    public async changeTicketDuration(ticketId: number, body: { duration: number }) {
        const response = await axios.post<void>(`${API_URL}/ticket/${ticketId}/review`, body, {
            headers: authHeader(),
        });

        return response.data;
    }

    public async createSprint(body: CreateSprintBody): Promise<Sprint> {
        // return sprint;

        const response = await axios.post<Sprint>(`${API_URL}/sprint`, body, {
            headers: authHeader(),
        });

        return response.data;
    }

    public async getLatestSprint(): Promise<Sprint> {
        return sprint;

        const response = await axios.get<Sprint>(`${API_URL}/sprint`, {
            headers: authHeader(),
        });

        return response.data;
    }

    public async getAllUsers(): Promise<Worker[]> {
        // return [
        //     {
        //         id: 1,
        //         email: 'email',
        //         username: 'username',
        //         is_active: true,
        //         is_superuser: true,
        //         created_at: '2021-01-01',
        //         updated_at: '2021-01-01',
        //     },
        //     {
        //         id: 2,
        //         email: 'email2',
        //         username: 'username2',
        //         is_active: true,
        //         is_superuser: true,
        //         created_at: '2021-01-01',
        //         updated_at: '2021-01-01',
        //     },
        // ];

        const response = await axios.get<Worker[]>(`${API_URL}/user/all`, {
            headers: authHeader(),
        });

        return response.data;
    }
}

export const TicketApiServiceInstanse = new TicketApiService();
