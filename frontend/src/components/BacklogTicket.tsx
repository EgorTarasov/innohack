import { Button, Card, Col, Row, Tag, Typography } from 'antd';
import { Ticket } from '../api/models';
import { FireFilled } from '@ant-design/icons';
import Priority from './Priority';
import { useStores } from '../hooks/useStores';
import { observer } from 'mobx-react-lite';

type Props = {
    ticket: Ticket;
    isDeleteAvailable?: boolean;
    isAddAvailable?: boolean;
    ticketIndex?: number;
};

const BacklogTicket = observer(
    ({ ticket, isDeleteAvailable, isAddAvailable, ticketIndex }: Props) => {
        const { rootStore } = useStores();

        return (
            <Card className='ticket'>
                <Row justify={'space-between'}>
                    <Col span={16}>
                        <Typography.Title className='title-5' level={5}>
                            {ticket.title}
                        </Typography.Title>
                    </Col>

                    <Col span={8}>
                        <Row justify={'end'} gutter={5}>
                            <Col>
                                <Tag className='tag tag__skill' color='#0277ff'>
                                    {ticket.roles.label}
                                </Tag>
                            </Col>
                            <Col>
                                <Tag className='tag tag__level' color='#8024C0'>
                                    {ticket.level.label}
                                </Tag>
                            </Col>
                        </Row>
                    </Col>
                </Row>

                <Row style={{ marginTop: 10 }}>
                    <Col span={24}>
                        <Typography.Paragraph>{ticket.description}</Typography.Paragraph>
                    </Col>
                </Row>

                <Row style={{ marginBottom: 10 }}>
                    <Priority priorityId={ticket.priority} />
                </Row>

                <Row align={'middle'}>
                    <FireFilled style={{ color: '#0A0A0A' }} />

                    <Typography.Paragraph style={{ marginBottom: 0, marginLeft: 10 }}>
                        <b>Дедлайн</b> — {new Date(ticket.due_date).toLocaleDateString()}
                    </Typography.Paragraph>
                </Row>

                <Row>
                    <Typography.Paragraph style={{ color: '#0277ff', fontSize: 16, marginTop: 20 }}>
                        Время выполнения:{' '}
                        <span style={{ fontSize: 18 }}>
                            {ticket.durations?.length && ticket.durations[0]}-
                            {ticket.durations?.length &&
                                ticket.durations[ticket.durations.length - 1]}{' '}
                        </span>
                        story points
                    </Typography.Paragraph>
                </Row>

                {isDeleteAvailable && (
                    <Row>
                        <Button type='primary' danger style={{ marginTop: 20 }}>
                            Удалить
                        </Button>
                    </Row>
                )}

                {isAddAvailable && (
                    <Row>
                        <Button
                            type='primary'
                            style={{ marginTop: 20 }}
                            onClick={() =>
                                rootStore.addTicketToSprintByUser(
                                    rootStore.activeSprintUserIndex,
                                    ticketIndex || 0,
                                    ticket
                                )
                            }
                        >
                            Добавить в спринт для{' '}
                            {
                                rootStore.sprint?.users[rootStore.activeSprintUserIndex].user_data
                                    .username
                            }
                        </Button>
                    </Row>
                )}
            </Card>
        );
    }
);

export default BacklogTicket;
