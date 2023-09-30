import { Col, Layout, Row, Tabs, TabsProps, Tag } from 'antd';
import { Content, Header } from 'antd/es/layout/layout';
import ReviewList from '../components/ReviewList';
import BacklogList from '../components/BacklogList';
import { useEffect } from 'react';
import { useStores } from '../hooks/useStores';
import Sprint from '../components/Sprint';
import { Link } from 'react-router-dom';
import { LogoutOutlined } from '@ant-design/icons';
import AuthService from '../api/AuthService';
import Statistics from '../components/Statistics';

const items: TabsProps['items'] = [
    {
        key: '1',
        label: 'Оценка задач',
        children: <ReviewList />,
    },
    {
        key: '2',
        label: 'Бэклог',
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
        children: <Statistics />,
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
                        justifyContent: 'end',
                        background: '#ffffff',
                        borderBottom: '1px solid #e8e8e8',
                    }}
                >
                    <Col>
                        <span style={{ marginLeft: 10 }}>
                            Роль:{' '}
                            <Tag className='tag tag__skill' color='#0277ff'>
                                Backend
                            </Tag>
                        </span>

                        <Link
                            onClick={() => {
                                AuthService.logout();

                                setTimeout(() => {
                                    window.location.href = '/login';
                                }, 100);
                            }}
                            to='/login'
                            style={{ marginLeft: 20 }}
                        >
                            <LogoutOutlined style={{}} />
                        </Link>
                    </Col>
                </Header>
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
