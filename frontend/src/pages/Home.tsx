import { Col, Layout, Row, Tabs, TabsProps } from 'antd';
import { Content, Header } from 'antd/es/layout/layout';
import ReviewList from '../components/ReviewList';
import BacklogList from '../components/BacklogList';
import { useEffect } from 'react';
import { useStores } from '../hooks/useStores';
import Sprint from '../components/Sprint';

const items: TabsProps['items'] = [
    {
        key: '1',
        label: 'Оценка задач',
        children: <ReviewList />,
    },
    {
        key: '2',
        label: 'Беклог',
        children: <BacklogList />,
    },
];

const sprintItems: TabsProps['items'] = [
    {
        key: '1',
        label: 'Текущий спринт',
        children: <Sprint />,
    },
    {
        key: '2',
        label: 'Статистика',
        children: 'Статистика',
    },
];

const Home = () => {
    const { rootStore } = useStores();

    useEffect(() => {
        async function fetchBacklog() {
            await rootStore.getTickets();
        }
        fetchBacklog();
    }, [rootStore]);

    return (
        <>
            <Layout style={{ background: '#ffffff' }}>
                <Header
                    style={{
                        position: 'sticky',
                        top: 0,
                        zIndex: 1,
                        width: '100%',
                        display: 'flex',
                        alignItems: 'center',
                        background: '#ffffff',
                    }}
                ></Header>
                <Content style={{ padding: '0 50px' }}>
                    <Row gutter={50}>
                        <Col span={12}>
                            <Tabs defaultActiveKey='1' items={items} />
                        </Col>
                        <Col span={12}>
                            <Tabs defaultActiveKey='1' items={sprintItems} />
                        </Col>
                    </Row>
                </Content>
            </Layout>
        </>
    );
};

export default Home;
