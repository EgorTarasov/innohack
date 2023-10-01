import { Col, Row, Tooltip } from 'antd';
import { SprintI } from '../api/models';

type Props = {
    sprint: SprintI | null;
};

const SprintTimeline = ({ sprint }: Props) => {
    let tileBackground = '#67ADFF';

    return (
        <>
            {sprint &&
                sprint.users.map((user) => (
                    <Row gutter={5}>
                        <Col style={{ display: 'flex', alignItems: 'center' }} span={5}>
                            {user.user_data.username}
                        </Col>
                        <Col span={19}>
                            <Row>
                                {user.tickets.map((ticket) => {
                                    const width =
                                        (1 / user.tickets.length) *
                                        (Math.random() * 0.3 + 0.7) *
                                        100;

                                    tileBackground =
                                        tileBackground === '#67ADFF' ? '#0277FF' : '#67ADFF';

                                    return (
                                        <Tooltip title={ticket.title}>
                                            <div
                                                style={{
                                                    width: `${width}%`,
                                                    background: tileBackground,
                                                }}
                                                className='timeline-tile'
                                            >
                                                {ticket.id}
                                            </div>
                                        </Tooltip>
                                    );
                                })}
                            </Row>
                        </Col>
                    </Row>
                ))}
        </>
    );
};

export default SprintTimeline;
