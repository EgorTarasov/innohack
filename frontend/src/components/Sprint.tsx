import { PlusSquareOutlined } from '@ant-design/icons';
import { Button, Col, Form, Input, InputNumber, Modal, Row, Select, Typography } from 'antd';
import { useEffect, useState } from 'react';
import { useStores } from '../hooks/useStores';
import { CreateSprintBody, Worker } from '../api/models';

const Sprint = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [confirmLoading, setConfirmLoading] = useState(false);
    const { rootStore } = useStores();
    const [form] = Form.useForm();
    const [users, setUsers] = useState<Worker[]>([]);

    useEffect(() => {
        async function fetchUsers() {
            const fetchedUsers = await rootStore.getAllUsers();
            setUsers(fetchedUsers);
        }
        fetchUsers();
    }, [rootStore]);

    const showModal = () => {
        setIsModalOpen(true);
    };

    const handleOk = async () => {
        console.log('handleOk');

        setConfirmLoading(true);

        const values = form.getFieldsValue();

        const usersHours: { id: number; hours: number }[] = [];

        Object.keys(values).forEach((key) => {
            if (key.startsWith('users')) {
                usersHours.push({
                    id: Number(key.split('.')[1]),
                    hours: 40,
                });
            }
        });

        const body: CreateSprintBody = {
            duration: values.duration || 1,
            target: values.target || '',
            users: usersHours,
        };

        console.log(body);

        await rootStore.createSprint(body).finally(() => {
            setConfirmLoading(false);
            setIsModalOpen(false);
        });
    };

    const handleCancel = () => {
        setIsModalOpen(false);
    };

    return (
        <>
            <Row>
                <Col span={24}>
                    <Button
                        className='button_secondary'
                        type='primary'
                        onClick={showModal}
                        icon={<PlusSquareOutlined />}
                    >
                        Создать спринт
                    </Button>
                    <Modal
                        title='Новый спринт'
                        open={isModalOpen}
                        onCancel={handleCancel}
                        confirmLoading={confirmLoading}
                        footer={[
                            <Button key='back' onClick={handleCancel}>
                                Отмена
                            </Button>,
                            <Button form='create-sprint' key='submit' htmlType='submit'>
                                Создать спринт
                            </Button>,
                        ]}
                    >
                        <Form
                            form={form}
                            name='create-sprint'
                            onFinish={handleOk}
                            initialValues={{
                                remember: true,
                            }}
                        >
                            <Form.Item
                                name='target'
                                rules={[
                                    {
                                        required: true,
                                        message: 'Пожалуйста, введите цель спринта',
                                    },
                                ]}
                            >
                                <Input
                                    style={{ borderBottom: '1px solid rgba(10,10,10,0.32)' }}
                                    bordered={false}
                                    size='large'
                                    placeholder='Цель спринта'
                                />
                            </Form.Item>

                            <Typography.Title className='title-5' level={5}>
                                Загруженность членов команды
                            </Typography.Title>

                            {users.map((user) => (
                                <Form.Item
                                    key={user.id}
                                    name={`users.${user.id}`}
                                    label={user.username}
                                >
                                    <InputNumber min={0} max={100} defaultValue={40} />
                                </Form.Item>
                            ))}

                            <Form.Item
                                name='duration'
                                label='Длительность спринта'
                                rules={[
                                    {
                                        message: 'Пожалуйста, введите длительность спринта',
                                    },
                                ]}
                                className='sh-select'
                            >
                                <Select
                                    bordered={false}
                                    placeholder='Длительность спринта'
                                    size='large'
                                    defaultValue={'1'}
                                    style={{ borderBottom: '1px solid rgba(10,10,10,0.32)' }}
                                >
                                    <Select.Option value='1'>1 неделя</Select.Option>
                                    <Select.Option value='2'>2 недели</Select.Option>
                                    <Select.Option value='3'>3 недели</Select.Option>
                                    <Select.Option value='4'>4 недели</Select.Option>
                                </Select>
                            </Form.Item>
                        </Form>
                    </Modal>
                </Col>
            </Row>
        </>
    );
};

export default Sprint;
