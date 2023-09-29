import { User } from '../../models/User';

export interface RegisterResponse {
    bearer_token: string;
    user: User;
}
