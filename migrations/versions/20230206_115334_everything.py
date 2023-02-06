"""everything

Revision ID: 6ff2a7b7a5e7
Revises: 
Create Date: 2023-02-06 11:53:34.568353

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '6ff2a7b7a5e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creatorId', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('state', sa.String(length=255), nullable=False),
    sa.Column('country', sa.String(length=255), nullable=False),
    sa.Column('imageUrl', sa.String(length=1000), nullable=False),
    sa.Column('videoUrl', sa.String(length=1000), nullable=True),
    sa.Column('fundingGoal', sa.DECIMAL(precision=50, scale=2), nullable=False),
    sa.Column('startDate', sa.String(length=50), nullable=False),
    sa.Column('endDate', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=4000), nullable=False),
    sa.Column('risks', sa.String(length=4000), nullable=False),
    sa.ForeignKeyConstraint(['creatorId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    if environment == "production":
        op.execute(f"ALTER TABLE projects SET SCHEMA {SCHEMA};")
        
    op.create_table('rewards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=50, scale=2), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.Column('projectId', sa.Integer(), nullable=False),
    sa.Column('estimatedDelivery', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['projectId'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    if environment == "production":
        op.execute(f"ALTER TABLE rewards SET SCHEMA {SCHEMA};")
        
    op.create_table('pledges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rewardId', sa.Integer(), nullable=True),
    sa.Column('projectId', sa.Integer(), nullable=True),
    sa.Column('backerId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['backerId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['projectId'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['rewardId'], ['rewards.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    if environment == "production":
        op.execute(f"ALTER TABLE pledges SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pledges')
    op.drop_table('rewards')
    op.drop_table('projects')
    op.drop_table('users')
    # ### end Alembic commands ###