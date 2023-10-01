export interface User {
    id: number;
    login: string;
    name: string;
}

export interface Worker {
    id: number;
    email: string;
    username: string;
    is_active: boolean;
    is_superuser: boolean;
    created_at: string;
    updated_at: string;
}
