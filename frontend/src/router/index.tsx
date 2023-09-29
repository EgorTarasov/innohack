import { createBrowserRouter } from 'react-router-dom';

import Home from '../pages/Home';

export const router = createBrowserRouter([
    // {
    //     path: '/signup',
    //     element: (
    //         <UnauthorizedOnlyRoute isSignedIn={AuthService.isAuthorized()}>
    //             <SignUp />
    //         </UnauthorizedOnlyRoute>
    //     ),
    // },
    // {
    //     path: '/login',
    //     element: (
    //         <UnauthorizedOnlyRoute isSignedIn={AuthService.isAuthorized()}>
    //             <Login />
    //         </UnauthorizedOnlyRoute>
    //     ),
    // },

    // {
    //     path: '*',
    //     element: (
    //         <ProtectedRoute isSignedIn={false}>
    //             <Home />
    //         </ProtectedRoute>
    //     ),
    // },
    {
        path: '*',
        element: <Home />,
    },
]);
