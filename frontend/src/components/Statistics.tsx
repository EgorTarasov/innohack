import { Col, Row, Typography } from 'antd';

const Statistics = () => {
    return (
        <>
            <Row gutter={20}>
                <Col span={12}>
                    <div className='statistics statistics__main'>
                        <div className='statistics__title'>96%</div>
                        <Typography.Paragraph className='statistics__value'>
                            Средняя успешность составления спинтов
                        </Typography.Paragraph>
                    </div>
                </Col>
                <Col span={12}>
                    <div className='statistics statistics__main'>
                        <div className='statistics__title'>3</div>
                        <Typography.Paragraph className='statistics__value'>
                            Спринтов были экспортированы без изменений{' '}
                        </Typography.Paragraph>
                    </div>
                </Col>
            </Row>
            <Row style={{ marginTop: 20 }} gutter={20}>
                <Col span={12}>
                    <div className='statistics statistics__secondary'>
                        <div className='statistics__title'>5</div>
                        <Typography.Paragraph className='statistics__value'>
                            Спринтов с малыми <br /> изменениями
                        </Typography.Paragraph>
                    </div>
                </Col>
                <Col span={12}>
                    <div className='statistics statistics__secondary'>
                        <div className='statistics__title'>2</div>
                        <Typography.Paragraph className='statistics__value'>
                            Спринтов с сильными <br /> изменениями
                        </Typography.Paragraph>
                    </div>
                </Col>
            </Row>
        </>
    );
};

export default Statistics;
