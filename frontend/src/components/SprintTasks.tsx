import { Button, Col, Row, Segmented, Typography } from 'antd';
import { SprintI } from '../api/models';
import BacklogTicket from './BacklogTicket';
import { useState } from 'react';
import { SegmentedValue } from 'antd/es/segmented';
import SprintTimeline from './SprintTimeline';
import { EditOutlined } from '@ant-design/icons';
import { useStores } from '../hooks/useStores';
import { observer } from 'mobx-react-lite';

type Props = {
    sprint: SprintI | null;
};

const SprintTasks = observer(({ sprint }: Props) => {
    const [segmentedValue, setSegmentedValue] = useState('Карточки задач');
    const { rootStore } = useStores();

    const onSegmentedChange = (value: SegmentedValue) => {
        setSegmentedValue(value as string);
    };

    const onEditClick = (index: number) => {
        rootStore.setActiveSprintUserIndex(index);
        rootStore.setIsAddTicketAvailable(true);
    };

    return (
        <>
            {rootStore.sprint && (
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
                                    Цель спринта: {rootStore.sprint.target}
                                </Typography.Title>
                            </Row>

                            {rootStore.sprint.users.map((user, index) => (
                                <Row key={index} style={{ marginTop: 30 }}>
                                    <Col span={24}>
                                        <Row justify={'space-between'} align={'middle'}>
                                            <Col>
                                                <Typography.Title level={5}>
                                                    {user.user_data.username}:{' '}
                                                    {user.user_data.hours} часов
                                                </Typography.Title>
                                            </Col>

                                            <Col>
                                                <Button
                                                    style={{ marginBottom: 5 }}
                                                    icon={<EditOutlined />}
                                                    onClick={() => onEditClick(index)}
                                                ></Button>
                                            </Col>
                                        </Row>

                                        <div>
                                            {user.tickets.map((ticket, index) => (
                                                <BacklogTicket key={index} ticket={ticket} />
                                            ))}
                                        </div>
                                    </Col>
                                </Row>
                            ))}
                        </>
                    )}

                    <div style={{ marginTop: 30 }}>
                        {segmentedValue === 'Таймлайн' && <SprintTimeline sprint={sprint} />}
                    </div>
                </>
            )}
        </>
    );
});

export default SprintTasks;
