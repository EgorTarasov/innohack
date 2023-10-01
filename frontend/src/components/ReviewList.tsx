import { useEffect } from 'react';
import { Ticket } from '../api/models';
import { useStores } from '../hooks/useStores';
import ReviewTicket from './ReviewTicket';
import { observer } from 'mobx-react-lite';

const ReviewList = observer(() => {
    const { rootStore } = useStores();

    useEffect(() => {
        async function fetchBacklog() {
            await rootStore.getTicketsByUserRole(1);
        }
        fetchBacklog();
    }, [rootStore]);

    return (
        <div>
            {rootStore.ticketsByUserRole.map((ticket: Ticket) => (
                <ReviewTicket key={ticket.id} ticket={ticket} />
            ))}
        </div>
    );
});

export default ReviewList;
