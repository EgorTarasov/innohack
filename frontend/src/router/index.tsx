import { createBrowserRouter } from 'react-router-dom';

import Home from '../pages/Home';
import UnauthorizedOnlyRoute from './UnauthorizedOnlyRoute';
import AuthService from '../api/AuthService';
import SignUp from '../pages/SignUp';
import Login from '../pages/Login';
import ProtectedRoute from './ProtectedRoute';

export const router = createBrowserRouter([
    {
        path: '/signup',
        element: (
            <UnauthorizedOnlyRoute isSignedIn={AuthService.isAuthorized()}>
                <SignUp />
            </UnauthorizedOnlyRoute>
        ),
    },
    {
        path: '/login',
        element: (
            <UnauthorizedOnlyRoute isSignedIn={AuthService.isAuthorized()}>
                <Login />
            </UnauthorizedOnlyRoute>
        ),
    },
    {
        path: '/home',
        element: (
            <ProtectedRoute isSignedIn={AuthService.isAuthorized()}>
                <Home />
            </ProtectedRoute>
        ),
    },
    {
        path: '*',
        element: (
            <ProtectedRoute isSignedIn={AuthService.isAuthorized()}>
                <Home />
            </ProtectedRoute>
        ),
    },
]);
