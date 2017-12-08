# -*- coding: utf-8 -*-

{
    'name': 'Discuss',
    'version': '1.0',
    'category': 'Discuss',
    'sequence': 25,
    'summary': 'Discussions, Mailing Lists, News',
    'description': "",
    'website': 'https://www.odoo.com/page/enterprise-social-network',
    'depends': ['base', 'base_setup', 'bus', 'web_tour'],
    'data': [
        'wizard/invite_view.xml',
        'wizard/mail_compose_message_view.xml',
        'views/mail_message_subtype_views.xml',
        'views/mail_tracking_views.xml',
        'views/mail_message_views.xml',
        'views/mail_mail_views.xml',
        'views/mail_followers_views.xml',
        'views/mail_channel_views.xml',
        'views/mail_shortcode_views.xml',
        'views/mail_activity_views.xml',
        'views/res_config_settings_views.xml',
        'data/mail_data.xml',
        'data/mail_channel_data.xml',
        'data/mail_shortcode_data.xml',
        'data/mail_activity_data.xml',
        'security/mail_security.xml',
        'security/ir.model.access.csv',
        'views/mail_alias_views.xml',
        'views/res_users_views.xml',
        'views/mail_templates.xml',
        'wizard/email_template_preview_view.xml',
        'views/mail_template_views.xml',
        'views/ir_actions_views.xml',
        'views/ir_model_views.xml',
        'views/res_partner_views.xml',
    ],
    'demo': [
        'data/mail_demo.xml',
        'data/mail_channel_demo.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/activity.xml',
        'static/src/xml/client_action.xml',
        'static/src/xml/composer.xml',
        'static/src/xml/chatter.xml',
        'static/src/xml/followers.xml',
        'static/src/xml/systray.xml',
        'static/src/xml/thread.xml',
        'static/src/xml/chat_window.xml',
        'static/src/xml/extended_chat_window.xml',
        'static/src/xml/announcement.xml',
        'static/src/xml/web_kanban_activity.xml',
    ],
}