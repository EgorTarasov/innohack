import { FireFilled } from '@ant-design/icons';
import { Button, Card, Col, InputNumber, Row, Space, Tag, Typography } from 'antd';
import { Ticket } from '../api/models';

type Props = {
    ticket: Ticket;
};

const ReviewTicket = ({ ticket }: Props) => {
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
                        <Button type='primary'>Задать</Button>
                    </Space.Compact>
                </Col>

                <Col>
                    <Button type='default'>Не готов выполнить</Button>
                </Col>
            </Row>
        </Card>
    );
};

export default ReviewTicket;
