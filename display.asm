assume cs:code,ds:data,es:display,ss:stack

data segment
	db 'Welcome to masm!'	
	db 02h,24h,71h
data ends

stack segment
	db 16 dup(0)
stack ends

display segment
	db 1024 dup(0)
display ends

code segment

start:
	mov ax,data
	mov ds,ax
	mov si,0			;si指向写入的位置
	mov ax,0b872h		;定位显示位置
	mov es,ax
	mov cx,3			;3次外循环，一次显示一行
	mov di,0			;di指向显示属性参数
	
s0: 
	push cx
	push ax
	mov cx,16			;16次字符写入循环
	mov bx,0
	
s:
	mov al,[bx]			;data:0000位的字符写入
	mov es:[si],al		;写入到显示缓存
	mov al,[di+10h]     ;指向显示属性
	mov es:[si+1],al	;写入显示属性到显示缓存
	add si,2
	inc bx
  loop s
	
	sub si,32			;重新指向00位置(归位操作)
	add si,160			;换行，因为一行160个字节
	pop ax
	pop cx
	inc di				;改变颜色
  loop s0
	
	mov ax,4c00h
	int 21h
	
code ends

end start
	
	