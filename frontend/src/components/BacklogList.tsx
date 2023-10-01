import { observer } from 'mobx-react-lite';
import BacklogTicket from './BacklogTicket';
import { useStores } from '../hooks/useStores';
import { Button } from 'antd';
import { ImportOutlined } from '@ant-design/icons';
import { useState } from 'react';

const BacklogList = observer(() => {
    const { rootStore } = useStores();
    const [loading, setLoading] = useState(false);

    return (
        <div>
            <Button
                onClick={() => {
                    setLoading(true);
                    rootStore.importTickets().finally(() => setLoading(false));
                }}
                loading={loading}
                icon={<ImportOutlined />}
            >
                Загрузить задачи из TeamFlame
            </Button>

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
