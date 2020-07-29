from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def make(paginator):
	pager = ''
	
	if paginator.has_previous():
		pager = '<a href="?page=' + str(paginator.previous_page_number()) + '" class=""><i class="fas fa-caret-left"></i></a>'
	else:
		pager = '<span class="disabled"><i class="fas fa-caret-left"></i></span>'
	
	for num in paginator.paginator.page_range:
		linknum = str(num)
		if paginator.number == num:
			pager = pager + '<span class=" current">' + linknum + '</span>'
		else:
			pager = pager + '<a href="?page=' + linknum + '" class="">' + linknum + '</a>'
	
	if paginator.has_next():
		pager = pager + '<a href="?page=' + str(paginator.next_page_number()) + '" class=""><i class="fas fa-caret-right"></i></a>'
	else:
		pager = pager + '<span><i class="fas fa-caret-right"></i></span>'
	
	
	return mark_safe(pager)