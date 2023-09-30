import { Col, Row, Segmented, Typography } from 'antd';
import { Sprint } from '../api/models';
import BacklogTicket from './BacklogTicket';
import { useState } from 'react';
import { SegmentedValue } from 'antd/es/segmented';

type Props = {
    sprint: Sprint | null;
};

const SprintTasks = ({ sprint }: Props) => {
    const [segmentedValue, setSegmentedValue] = useState('Карточки задач');

    const onSegmentedChange = (value: SegmentedValue) => {
        setSegmentedValue(value as string);
    };

    return (
        <>
            {sprint && (
                <>
                    <Row>
                        <Segmented
                            style={{ marginTop: 20, background: 'rgba(2, 119, 255, 0.12)' }}
                            size='large'
                            options={['Карточки задач', 'Таймлайн']}
                            onChange={(value) => onSegmentedChange(value)}
                        />
                    </Row>

                    {segmentedValue === 'Карточки задач' && (
                        <>
                            <Row>
                                <Typography.Title
                                    style={{ marginTop: 20 }}
                                    className='title-5'
                                    level={5}
                                >
                                    Цель спринта: {sprint.target}
                                </Typography.Title>
                            </Row>

                            {sprint.users.map((user) => (
                                <Row style={{ marginTop: 30 }}>
                                    <Col span={24}>
                                        <Row>
                                            <Typography.Title level={5}>
                                                {user.user_data.username}: {user.user_data.hours}{' '}
                                                часов
                                            </Typography.Title>
                                        </Row>

                                        <div>
                                            {user.tickets.map((ticket) => (
                                                <BacklogTicket ticket={ticket} />
                                            ))}
                                        </div>
                                    </Col>
                                </Row>
                            ))}
                        </>
                    )}

                    {segmentedValue === 'Таймлайн' && 'тайлайн'}
                </>
            )}
        </>
    );
};

export default SprintTasks;
