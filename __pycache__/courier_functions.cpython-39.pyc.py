a
    o�`�  �                   @   s4   d dl Z dd� Zdd� Zdd� Zdd	� Zd
d� ZdS )�    Nc                  C   s&   t dd�} | �� }t|� | ��  d S )Nzdata/couriermenu.txt�r)�open�read�print�close)�fileZcouriermenu� r   �9/Users/francescowang/Desktop/project/courier_functions.py�print_courier_menu   s    
r
   c                 C   s�   t ��  t| � i }td�}|�� dkr,d S td|�� �� � d��}|�� �� |d< |�� |d< | �|� td� t| � td� | S d S )	Nz;
Press 0 to go back.

What courier would you like to add?

�0z
What is the z's telephone number? �Courier�Telephone Number�
Couriers:
�
)�core�function_clear�print_vertical�input�strip�title�appendr   )�courier_listZadd_courier_entry�user_add_inputZcourier_numr   r   r	   �courier_add   s     �
r   c                 C   s�   t ��  t| � td�}|�� dkr(d S | D ]p}|d |�� �� kr,td|�� �� � d��}|dkrt|�� �� |d< td�}|dkr�|�� |d< nq,td	� q,d S )
Nz?
Press 0 to go back.

Which courier would you like to update?

r   r   zWho would you like to update z to? Press Enter to skip. � zLWhat would you like to update the telephone number to? Press Enter to skip. r   �S
We apologise for this inconvenience. We do not have this courier in our database.
)r   r   r   r   r   r   r   )r   �user_update_input�courierZupdated_oneZ
new_numberr   r   r	   �courier_update'   s"    �r   c                 C   s�   t ��  t| � td�}|�� dkr(d S | D ]N}|d |�� �� kr,| �|�}| �|� td� t| � td� |   S q,q,td� d S )Nz?
Press 0 to go back.

Which courier would you like to delete?

r   r   r   r   r   )	r   r   r   r   r   r   �index�popr   )r   �user_delete_inputr   Zcourier_indexr   r   r	   �courier_deleteB   s"    �

r"   c                 C   s\   t t| ��D ]B}d|� d�}| | �� D ]\}}||� d|� d�7 }q(t|� qtd� d S )NzCourier r   z: )�range�len�itemsr   )r   �vertical�str�key�valuer   r   r	   r   ^   s    
r   )r   r
   r   r   r"   r   r   r   r   r	   �<module>   s
   