import { Card, Col, Row, Tag, Typography } from 'antd';
import { Ticket } from '../api/models';
import { FireFilled } from '@ant-design/icons';
import Priority from './Priority';

type Props = {
    ticket: Ticket;
};

const BacklogTicket = ({ ticket }: Props) => {
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
                                {ticket.role.label}
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
                    <b>Дедлайн</b> — {ticket.due_date}
                </Typography.Paragraph>
            </Row>

            <Row>
                <Typography.Paragraph style={{ color: '#0277ff', fontSize: 16, marginTop: 20 }}>
                    Время выполнения:{' '}
                    <span style={{ fontSize: 18 }}>
                        {ticket.durations?.length && ticket.durations[0]}-
                        {ticket.durations.length && ticket.durations[ticket.durations.length - 1]}{' '}
                    </span>
                    story points
                </Typography.Paragraph>
            </Row>
        </Card>
    );
};

export default BacklogTicket;
