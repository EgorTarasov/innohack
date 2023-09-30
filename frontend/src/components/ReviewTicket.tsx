import { FireFilled } from '@ant-design/icons';
import { Button, Card, Col, InputNumber, Row, Space, Tag, Typography, message } from 'antd';
import { Ticket } from '../api/models';
import { useStores } from '../hooks/useStores';
import { useState } from 'react';

type Props = {
    ticket: Ticket;
};

const ReviewTicket = ({ ticket }: Props) => {
    const [messageApi, contextHolder] = message.useMessage();
    const { rootStore } = useStores();
    const [isDurationLoading, setIsDurationLoading] = useState(false);

    return (
        <>
            {contextHolder}
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

                <Row align={'middle'}>
                    <FireFilled style={{ color: '#0A0A0A' }} />

                    <Typography.Paragraph style={{ marginBottom: 0, marginLeft: 10 }}>
                        <b>Дедлайн</b> — {ticket.due_date}
                    </Typography.Paragraph>
                </Row>

                <Row style={{ marginTop: 20 }} justify={'space-between'}>
                    <Col>
                        <Space.Compact style={{ width: '100%' }}>
                            <InputNumber
                                style={{ width: 160 }}
                                min={1}
                                max={10}
                                placeholder='Время выполнения в сторипоинтах'
                            />
                            <Button
                                onClick={async () => {
                                    setIsDurationLoading(true);
                                    rootStore
                                        .changeTicketDuration(ticket.id, { duration: 1 })
                                        .then(() => {
                                            messageApi.success('Время изменено');
                                        })
                                        .catch(() => {
                                            messageApi.error('Ошибка изменения времени');
                                        })
                                        .finally(() => setIsDurationLoading(false));
                                }}
                                type='primary'
                                loading={isDurationLoading}
                            >
                                Задать
                            </Button>
                        </Space.Compact>
                    </Col>

                    <Col>
                        <Button type='default'>Не готов выполнить</Button>
                    </Col>
                </Row>
            </Card>
        </>
    );
};

export default ReviewTicket;
