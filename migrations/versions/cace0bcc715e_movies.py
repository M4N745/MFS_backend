"""movies & covers table

Revision ID: cace0bcc715e
Revises: 46d721ba70e5
Create Date: 2023-07-11 18:35:12.854557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cace0bcc715e'
down_revision = '46d721ba70e5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('covers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('path', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    default_cover_items = [
        { 'path': 'cover1.jpg' },
        { 'path': 'cover2.jpg' },
        { 'path': 'cover3.jpg' },
        { 'path': 'cover4.jpg' },
        { 'path': 'cover5.jpg' },
        { 'path': 'cover6.jpg' },
        { 'path': 'cover7.jpg' },
        { 'path': 'cover8.jpg' },
        { 'path': 'cover9.jpg' },
        { 'path': 'cover10.jpg' },
    ]
    covers_table = sa.table('covers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('path', sa.String(length=100), nullable=False),
    )
    op.bulk_insert(covers_table, default_cover_items)
    
    op.create_table('movies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.Column('cover_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['cover_id'], ['covers.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    default_movies_items = [
        { 'title': 'The Maze Runner', 'cover_id': 1, 'description': 'Thomas is deposited in a community of boys after his memory is erased, soon learning they are all trapped in a maze that will require him to join forces with fellow "runners" for a shot at escape' },
        { 'title': 'Maze Runner: The Scorch Trials', 'cover_id': 2, 'description': 'After having escaped the Maze, the Gladers now face a new set of challenges on the open roads of a desolate landscape filled with unimaginable obstacles.' },
        { 'title': 'Maze Runner: The Death Cure', 'cover_id': 3, 'description': 'Young hero Thomas embarks on a mission to find a cure for a deadly disease known as "The Flare".' },
        { 'title': 'The Fast and the Furious', 'cover_id': 4, 'description': "Los Angeles police officer Brian O'Conner must decide where his loyalty really lies when he becomes enamored with the street racing world he has been sent undercover to destroy." },
        { 'title': 'The Fast and the Furious: Tokyo Drift', 'cover_id': 5, 'description': 'A teenager becomes a major competitor in the world of drift racing after moving in with his father in Tokyo to avoid a jail sentence in America.' },
        { 'title': 'Peaky Blinders', 'cover_id': 6, 'description': 'A gangster family epic set in 1900s England, centering on a gang who sew razor blades in the peaks of their caps, and their fierce boss Tommy Shelby.' },
        { 'title': 'The Witcher', 'cover_id': 7, 'description': 'Geralt of Rivia, a solitary monster hunter, struggles to find his place in a world where people often prove more wicked than beasts.' },
        { 'title': 'The Walking Dead', 'cover_id': 8, 'description': 'Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive.' },
        { 'title': 'The Last of Us', 'cover_id': 9, 'description': "After a global pandemic destroys civilization, a hardened survivor takes charge of a 14-year-old girl who may be humanity's last hope." },
        { 'title': 'Mr. Robot', 'cover_id': 10, 'description': 'Elliot, a brilliant but highly unstable young cyber-security engineer and vigilante hacker, becomes a key figure in a complex game of global dominance when he and his shadowy allies try to take down the corrupt corporation he works for.' },
    ]
    
    movies_table = sa.table('movies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.Column('cover_id', sa.Integer(), nullable=True),    
    )
    op.bulk_insert(movies_table, default_movies_items)


def downgrade():
    op.drop_table('movies')
    op.drop_table('covers')
