import { Tag } from 'antd';

type Props = {
    priorityId: number;
};

const Priority = ({ priorityId }: Props) => {
    return (
        <>
            {priorityId === 1 && (
                <Tag className='tag tag__high-priority' color='#0277ff'>
                    высокий приоритет
                </Tag>
            )}

            {priorityId === 2 && (
                <Tag className='tag tag__medium-priority' color='#8024C0'>
                    средний приоритет
                </Tag>
            )}

            {priorityId >= 3 && (
                <Tag className='tag tag__low-priority' color='#FFB800'>
                    низкий приоритет
                </Tag>
            )}
        </>
    );
};

export default Priority;
