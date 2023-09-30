import axios from 'axios';
import { API_URL } from '../config';
import authHeader from '../utils/authHeader';
import { Ticket } from './models';

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
        return [
            {
                id: 1,
                sprint_id: 1,
                title: 'ticket by role',
                description: 'test',
                reporter_id: 1,
                assignee_id: 2,
                due_date: '2021-01-01',
                durations: [1, 2, 4],
                role: { role_id: 1, label: 'Frontend' },
                level: { level_id: 1, label: 'Junior' },
                priority: 2,
            },
        ];

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
}

export const TicketApiServiceInstanse = new TicketApiService();
