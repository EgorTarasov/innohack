import { observer } from 'mobx-react-lite';
import BacklogTicket from './BacklogTicket';
import { useStores } from '../hooks/useStores';

const BacklogList = observer(() => {
    const { rootStore } = useStores();

    return (
        <div>
            {rootStore.tickets.map((ticket, index) => (
                <BacklogTicket
                    key={ticket.id}
                    ticket={ticket}
                    isAddAvailable={rootStore.isAddTicketAvailable}
                    ticketIndex={index}
                />
            ))}
        </div>
    );
});

export default BacklogList;
